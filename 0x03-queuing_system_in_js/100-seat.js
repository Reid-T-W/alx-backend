const { promisify } = require('util');
// Client to connect to Redis Server
import { createClient } from 'redis';

const client = createClient();
const getPromise = promisify(client.get).bind(client);
const setPromise = promisify(client.set).bind(client);

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));

// When launching the application, set the number of available to 50
async function main () {
    await setPromise('available_seats', 50);
}

main();

const reservationEnabled = true

async function reserveSeat(number) {
    await getPromise('available_seats').then(async (availableSeats) => {
        await setPromise('available_seats', (Number(availableSeats) - number));
    });   
}

async function getCurrentAvailableSeats() {

    let currentAvailableSeats = await getPromise('available_seats');
    return currentAvailableSeats;
}

// Creating a kue
var kue = require('kue')
const reserve_seat = kue.createQueue();

// Creating an express server
const express = require('express');
const app = express();
const port = 1245;

app.get('/available_seats', (req, res) => {
    getCurrentAvailableSeats().then((currentAvailableSeats) => {
        return res.send({"numberOfAvailableSeats": currentAvailableSeats});
    });
  })

app.get('/reserve_seat', (req, res) => {
    if (reservationEnabled === false) {
        return res.send({ "status": "Reservation are blocked" })
    }
    try {
        const reserveJob = reserve_seat.create('object', {number: 1}).save();
        reserveJob.on('complete',function() {
          console.log(`Seat reservation job ${reserveJob.id} completed`);
        }).on('failed', function(err){
            console.log(`Seat reservation job ${reserveJob.id} failed: ${err}`);
        })
        return res.send({ "status": "Reservation in process" });
    } catch {
        return res.send({ "status": "Reservation failed" });
    }
})

app.get('/process', (req, res) => {
    reserve_seat.process('object', async function(job, done){
        const currentAvailableSeats = await getCurrentAvailableSeats();
        if (currentAvailableSeats === 0) {
            reservationEnabled = false;
            const error = Error(`Not enough seats available`)
            done(error)
            return
        }
        await reserveSeat(job.data.number);
        done();
    })
    return res.send({ "status": "Queue processing" });  
})

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
})