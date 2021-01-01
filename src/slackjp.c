/*
* 
*  ____  _            _          _ ____   ___  _   _   ____                          
* / ___|| | __ _  ___| | __     | / ___| / _ \| \ | | |  _ \ __ _ _ __ ___  ___ _ __ 
* \___ \| |/ _` |/ __| |/ /  _  | \___ \| | | |  \| | | |_) / _` | '__/ __|/ _ \ '__|
*  ___) | | (_| | (__|   <  | |_| |___) | |_| | |\  | |  __/ (_| | |  \__ \  __/ |   
* |____/|_|\__,_|\___|_|\_\  \___/|____/ \___/|_| \_| |_|   \__,_|_|  |___/\___|_|   
*                                                                                   
* Copyright 2021, Brandt Damman
* Slack is a software application developed by Slack Technologies, Inc.  All rights reserved.
*
*/

#include <fcntl.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

sem_t fileLock;

int main() {

    sem_init(&fileLock, 0, 1);

    int threadCount = 5;
    pthread_t* threads = (pthread_t*)malloc(sizeof(pthread_t) * threadCount);

    return 0;
}