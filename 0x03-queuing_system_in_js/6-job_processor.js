var kue = require('kue')
const push_notification_code = kue.createQueue();
push_notification_code.process('object', function(job, done){
    sendNotification(job.data.phoneNumber, job.data.cmessage);
})
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}