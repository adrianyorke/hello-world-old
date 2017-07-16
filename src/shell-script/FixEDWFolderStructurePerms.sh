#!/bin/sh
#####################################################################################
# Purpose: Shell script to fix DataStage file share folder permissions on existing folders.
#
# Comments:
#
# Input Arguments : projectName (e.g. EDW_Dev)
#                   dataSourceCode (e.g. RTTJ)
#
# Return Code: 0 = SUCCESS
# 
# History:
# 2017.05.05 Adrian Yorke / OP - Initial version.
#####################################################################################

# check mandatory arguments have been provided.
if [ $# -ne 2 ]
then
    echo "Incorrect arguments specified."
    echo "Usage: `basename $0` [Project Name] [Data Source Code]"
    exit 1
fi ;

rootPath="/data/datastage";
projectName="$1";
dataSourceCode="$2";
defaultPerms="775";

echo "Changing permissions for 'in' folder for source system..."
chmod ${defaultPerms} "${rootPath}/${projectName}/in/${dataSourceCode}";
if [ $? -ne 0 ]
then
	echo "Error changing permissions to ${defaultPerms} for ${rootPath}/${projectName}/in/${dataSourceCode}";
	exit 1;
fi ;

echo "Changing permissions for 'archive' subfolder..."
chmod ${defaultPerms} "${rootPath}/${projectName}/in/${dataSourceCode}/archive";
if [ $? -ne 0 ]
then
	echo "Error changing permissions to ${defaultPerms} for ${rootPath}/${projectName}/in/${dataSourceCode}/archive";
	exit 1;
fi ;

echo "Changing permissions for 'loading' subfolder..."
chmod ${defaultPerms} "${rootPath}/${projectName}/in/${dataSourceCode}/loading";
if [ $? -ne 0 ]
then
	echo "Error changing permissions to ${defaultPerms} for ${rootPath}/${projectName}/in/${dataSourceCode}/loading";
	exit 1;
fi ;

echo "Changing permissions for 'out' folder for source system..."
chmod ${defaultPerms} "${rootPath}/${projectName}/out/${dataSourceCode}";
if [ $? -ne 0 ]
then
	echo "Error changing permissions to ${defaultPerms} for ${rootPath}/${projectName}/out/${dataSourceCode}";
	exit 1;
fi ;

exit 0
