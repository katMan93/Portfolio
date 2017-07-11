#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>

/* VmMalware Detector
Author: Dylan Fahr
*/

void fileCheck(const char *lFileName);
void vAttack(bool result);
int numCores();



int main (void) {			//Gnerates the entire attack and pieces together the information found
    char *lFileName = "/usr/bin/vmtoolsd"; 		//location of vmtools file which identifies the environmnet as a virtual machine within vmware workstation
    FileCheck(lFileName);			//detects the presence of vmtools file
    int core = numCores();			//determines the number of cores of CPU listed within the environment. 
	if(core == 1){
		vAttack(false); 			// if the machine has one core, it is a virtual machine, do nothing
	}
	else{
		vAttack(true);				//machine has more than one core, could by host system, commence attack
	}
    
    return 0;
}

void fileCheck(const char *lFileName){			//detects presence of vmtools file

    if(!access(lFileName, F_OK )){
        printf("The File %s\t was Found\n",lFileName);			//if the file is found, the prompt displays it and does not attack commences
        printf("This is a virtual machine");
        vAttack(false);
        
    }else{
        printf("The File %s\t not Found\n",lFileName);			//file is not found, commence attack
        vAttack(true);
    }
}
int numCores(){ 						//determines number of CPU cores within the environment. Credit goes to author: Josh Willis for help coding this
	int cores = 0;
	char vInfo[50] = "/proc/cpuinfo";		//file location within Linux that contains information regarding CPU
	FILE *cpu = fopen(vInfo, "r");		// opens to detect if it is readable, which determines if existant on system
	char buff[50];
	fscanf(cpu, "%s", buff);
	while(strcmp(buff, "cores") != 0){		//scans and returns number of cores within CPU
		fscanf(cpu, "%s", buff);
	}
	fscanf(cpu, "%s", buff);
	fscanf(cpu, "%d", &cores);
	return cores;
}
void vAttack(bool result){			// attack on host machine if detected
	int i = 0;
	if (result = true){
		while(i == 0){
			printf(" Never gonna give you up / Never gonna let you down / Never gonna run around and desert you");		//repeates atack indefinately 
		}
	}
	else if (result = false){
		printf("Nothing to see here");		//not target machine, do not deploy attack
	}
}
