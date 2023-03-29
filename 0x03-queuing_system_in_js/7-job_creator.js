const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];
  var kue = require('kue')
  const push_notification_code_2 = kue.createQueue();

  for (const job of jobs) {
    const job = push_notification_code_2.create('object', job).save();

    job.on('complete',function() {
        console.log(`Notification job ${job.id} completed`);
    }).on('progress', function(progress) {
        console.log(`Notification job JOB_ID ${progress}% complete`)
    }).on('failed', function(err){
        console.log(`Notification job ${job.id} failed: ${err}`);
    }).on('enqueue', function(){
        console.log(`Notification job created: ${job.id}`);
    })
  }
