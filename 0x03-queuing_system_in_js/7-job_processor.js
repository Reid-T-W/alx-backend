var kue = require('kue')
const push_notification_code_2 = kue.createQueue();


push_notification_code_2.process('object', 10, function(job, done){
        sendNotification(job.data.phoneNumber, job.data.message, job, done);
})


function sendNotification(phoneNumber, message, job, done) {
    const blacklistedNumbers = [4153518780, 4153518781]
    job.progress(0, 100)
    // Converting phoneNumber to int
    phoneNumber = Number(phoneNumber)
    if (blacklistedNumbers.includes(phoneNumber)) {
        const error = Error(`Phone number ${phoneNumber} is blacklisted`)
        done(error)
        return
    }
    job.progress(50, 100).save()
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
    done();
}

