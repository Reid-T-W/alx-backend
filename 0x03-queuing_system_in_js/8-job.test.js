const assert =  require('assert');
import createPushNotificationsJobs from './8-job.js';
var kue = require('kue');
var queue = kue.createQueue();

describe('Testing queue', function() {
        before(function() {
            queue.testMode.enter();
        });

        beforeEach(function() {
            //Create the following job before each function call
            const jobs = [
                {
                    phoneNumber: '4153518780',
                    message: 'This is the code 1234 to verify your account'
                },
                {
                    phoneNumber: '4153518781',
                    message: 'This is the code 1235 to verify your account'
                }
            ];
            // Adding all jobs to the queue
            for (const job of jobs) {
                queue.createJob('myJob', job).save();
            }
        });

        afterEach(function() {
            queue.testMode.clear();
        });

        after(function() {
            queue.testMode.exit();
        });


    it('tests the length of the queue', function() {
        assert.equal(queue.testMode.jobs.length, 2);
    })
    it('testing the first element in the queue', function() {
        assert.equal(queue.testMode.jobs[0].data.phoneNumber, '4153518780');
        assert.equal(queue.testMode.jobs[0].data.message, 'This is the code 1234 to verify your account');
    })
    it('testing the second element in the queue', function() {
        assert.equal(queue.testMode.jobs[1].data.phoneNumber, '4153518781');
        assert.equal(queue.testMode.jobs[1].data.message, 'This is the code 1235 to verify your account');
    })
})





