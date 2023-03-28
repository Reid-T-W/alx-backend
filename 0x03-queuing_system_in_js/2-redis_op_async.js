import { createClient } from 'redis';
const util = require('util')

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

async function displaySchoolValue(schoolName) {
    const value = await client.get(schoolName)
    console.log(value);
}

//  promiseDisplaySchoolValue = util.promisify(displaySchoolValue)

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
