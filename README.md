# falcon-train

## Log into machine

-   triplecore aws login (`awslogintriplecore <MFA>` for me)
-   `aws ssm start-session --target <InstanceID>`

## get repo

-   `git clone https://github.com/triplecore-consulting/falcon-train.git`
-   `cd falcon-train`

## run setup

-   `bash ./setup.sh`
-   `LD_LIBRARY_PATH` is added to `.bashrc` Restart bash `exec bash` or
    logout/login
