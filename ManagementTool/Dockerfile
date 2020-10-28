FROM centos:7

USER root

RUN yum clean all \
    && yum repolist \
    && yum -y update \
    && yum -y reinstall glibc-common

RUN yum -y install tar unzip vi vim telnet net-tools curl openssl \
    && yum -y install apr apr-util apr-devel apr-util-devel \
    && yum -y install elinks locate python-setuptools \
    && yum -y install ntsysv httpd python3\
    && yum clean all

RUN pip3 install --upgrade pip
RUN pip3 install paramiko

RUN echo '1234' | passwd --stdin root 

ENV LANG=ko_KR.utf8 TZ=Asia/Seoul

EXPOSE 22