import { createClient } from 'redis'

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));
// client.on('quit', () => client.disconnect())
client.connect()


const listener = (message, channel) => {
    if (message === 'KILL_SERVER') {
        console.log(message)
        client.unsubscribe('holberton school channel', listener);
        // client.quit()
        client.disconnect()
        return;
    }
    else {
        console.log(message);
    }
}
client.subscribe('holberton school channel', listener);
