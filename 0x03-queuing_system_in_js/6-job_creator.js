var kue = require('kue')
const jobObject = {
    phoneNumber: "string",
    cmessage: "string",
}
const push_notification_code = kue.createQueue();
var job = push_notification_code.create('object', jobObject).save();

job.on('complete',function() {
    console.log('Notification job completed');
}).on('failed', function(){
    console.log('Job failed');
}).on('enqueue', function(){
    console.log(`Notification job created: ${job.id}`);
})