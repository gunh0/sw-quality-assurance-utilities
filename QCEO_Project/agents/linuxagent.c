#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>

#define BUFF_SIZE 1024

int client(int procnum, char **proc);

int main(int argc, char **argv) {
	while(1) {
		if(client(argc-1, argv) == -1) {
			perror("error: ");
			exit(0);
		}
		sleep(1);
	}
	return 0;
}


int client(int procnum, char **proc) {
	int i;
	int client_socket;
	struct sockaddr_in server_addr;
	char buff[BUFF_SIZE];
	FILE *fp;
	char strbuff[BUFF_SIZE];
	char result[BUFF_SIZE] = "Linux \n";


	client_socket = socket(PF_INET, SOCK_STREAM, 0);
	if(client_socket == -1) {
		printf("error : 소켓생성실패 \n");
		exit(1);
	}

	memset(&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = inet_addr("192.168.120.166");
	server_addr.sin_port = htons(4000);

	if(connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
		printf("error : 접속실패 \n");
		exit(1);
	}
	fp = popen("top -n 1 | grep -i cpu\\(s\\)| awk '{print $2+$4}'", "r");
	if(fp == NULL) {
		perror("error: ");
		exit(0);
	}
	fgets(strbuff, sizeof(strbuff), fp);
	strcat(result, strbuff);
	fclose(fp);

	fp = popen("free |grep -i Mem: | awk '{print $3/$2*100}'", "r");
	if(fp == NULL) {
		perror("error: ");
		exit(0);
	}
	fgets(strbuff, sizeof(strbuff), fp);
	strcat(result, strbuff);
	fclose(fp);

	for(i=1; i<procnum+1; i++) {
		char procstr[] = "ps -eo pmem,pcpu,cmd --sort -rss|grep ";
		char procstr2[] = "|sed -n 1p|awk '{print $1, $2}'";
		strcat(procstr, proc[i]);
		strcat(procstr, procstr2);
		fp = popen(procstr, "r");
		//printf("%s\n", procstr);
		if(fp == NULL) {
			perror("error: ");
			exit(0);
		}
		fgets(strbuff, sizeof(strbuff), fp);
		strcat(result, strbuff);		
		fclose(fp);
	}
	strcat(result, "\n");

	//printf("%lu", strlen(result));
	write(client_socket, result, strlen(result));
	
	return close(client_socket);
}
