function createPushNotificationsJobs(jobs, queue) {
    if (Array.isArray(jobs) === false) {
        throw (new Error('Jobs is not an array'));
    }
    for (const job of jobs) {
        const queuedJob = queue.create('object', job).save();
        
        queuedJob.on('complete',function() {
            console.log(`Notification job ${queuedJob.id} completed`);
        }).on('progress', function(progress) {
            console.log(`Notification job ${queuedJob.id} ${progress}% complete`)
        }).on('failed', function(err){
            console.log(`Notification job ${queuedJob.id} failed: ${err}`);
        }).on('enqueue', function(){
            console.log(`Notification job created: ${queuedJob.id}`);
        })
    }
}

module.exports = createPushNotificationsJobs