# falcon-train

## Launch instance from template

-   From template **LLMtrainingtest**
-   Make sure OS is **"Deep Learning AMI GPU PyTorch 2.0.1 (Ubuntu 20.04)"**
-   Select Instance type is **g5.xlarge**
-   **NOTE**: `falcon_pefty` will fail with a type error if more than one GPU is
    present
-   Make sure Security group **falcon** is selected
-   Set Storage volume size to (at least) **250GiB**
-   Click **Launch instance**

## Log into instance

-   triplecore aws login (`awslogintriplecore <MFA>` for me)
-   `aws ssm start-session --target <InstanceID>`

## get repo

-   `git clone https://github.com/triplecore-consulting/falcon-train.git`
-   `cd falcon-train`

## run setup

-   `bash ./setup.sh`
-   `LD_LIBRARY_PATH` is added to `.bashrc` Restart bash `exec bash` or
    logout/login

## run stuff manually

-   log into instance
-   `cd falcon-train`
-   `bash run.sh`

## run stuff automatically

-   ```
    aws ssm send-command --document-name "AWS-RunShellScript" --document-version "1" --targets '[{"Key":"InstanceIds","Values":["<INSTANCE_ID>"]}]' --parameters '{"workingDirectory":["/home/ssm-user/falcon-train"],"executionTimeout":["172800"],"commands":["bash ./run.sh"]}' --timeout-seconds 172800 --max-concurrency "50" --max-errors "0" --output-s3-bucket-name "triplecore-hc-exchange" --service-role-arn "arn:aws:iam::<ACCOUNT_ID>:role/<EC_TEMPLATE_ROLE>" --notification-config '{"NotificationArn":"arn:aws:sns:eu-central-1:<ACCOUNT_ID>:<TOPIC_NAME>","NotificationEvents":["All"],"NotificationType":"Command"}' --region eu-central-1
    ```

## TODO

-   run install as root
-   fix `LD_LIBRARY_PATH`
