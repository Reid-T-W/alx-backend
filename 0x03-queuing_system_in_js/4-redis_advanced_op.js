import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));
client.connect()

function setNewSchool(schoolName, value) {
    client.set(schoolName, value).then(() => {
        console.log('Reply: OK');
    }
)
}

function displaySchoolValue(schoolName) {
    client.get(schoolName).then((data) => {
        console.log(data);
    })
}

client.HSET('HolbertonSchools', 'Portland', 50).then(() => {
    console.log('Reply: 1');
})
client.HSET('HolbertonSchools', 'Seattle', 80).then(() => {
    console.log('Reply: 1');
})
client.HSET('HolbertonSchools', 'New York', 20).then(() => {
    console.log('Reply: 1');
})
client.HSET('HolbertonSchools', 'Bogota', 20).then(() => {
    console.log('Reply: 1');
})
client.HSET('HolbertonSchools', 'Cali', 40).then(() => {
    console.log('Reply: 1');
})
client.HSET('HolbertonSchools', 'Paris', 2).then(() => {
    console.log('Reply: 1');
})

client.hGetAll('HolbertonSchools').then((data) => {
    console.log(data);
})