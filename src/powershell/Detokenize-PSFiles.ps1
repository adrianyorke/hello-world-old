<#
.SYNOPSIS
   Detokenize DataStage Parameter Set Value Files.
.DESCRIPTION
   Detokenize DataStage Parameter Set Value Files and create _TEST version of the file in the same folder.
.EXAMPLE
   powershell -ExecutionPolicy ByPass -File ./Detokenize-PSFiles.ps1
.NOTES
	Author:  Adrian Yorke / OP
	Created: 30.05.2017
#>

cls

$DebugPreference = "Continue"

Write-Debug -Message 'Detokenizing DataStage Parameter Set Value Files...'

# TODO:
# . logging
# . CmdLet
# . Parameters (psetPath, filnamePattern)
# . Secure Copy (curl or PSCP-PuTTY Secure Copy)
# . Read tokenList from file

#$tokenList = Get-Content -Raw K:\Code\WindowsPowerShell\PS\TokenList_DEV-TEST.txt | ConvertFrom-StringData
#$tokenList = Get-Content K:\Code\WindowsPowerShell\PS\TokenList_DEV-TEST.txt | ConvertFrom-StringData
#$tokenList.GetType()

$tokenList = @{
	'<DB_ENV>'='D'
	;'<DS_PROJECT>'='EDW_Test'
	;'<DB_SERVER>'='jtytddbsr1'
	;'<DB_LOAD_PWD>'='{iisenc}8/7TgS2dM2bJqgR59u2y+A=='
	;'<DB_GCFR_PWD>'='{iisenc}pgv6a0fWKfsNyLge6qxAgNSIFaSI9o1ikzRO4SJgjBU='
}

$tokenList.GetType()

#$psetPath = 'K:\Temp\edw-release-2017.W21\ELEC-1.0\ParameterSet\Pset_Source_System'
#$psetPath = 'K:\Temp\edw-release-2017.W21\ELEC-1.0\ParameterSet\TD_GCFR_PS'
#$psetPath = 'K:\Temp\edw-release-2017.W21\ITU-1.0\ParameterSet\Pset_Source_System'
#$psetPath = 'K:\Temp\edw-release-2017.W21\ITU-1.0\ParameterSet\TD_GCFR_PS'
#$psetPath = 'K:\Temp\edw-release-2017.W21\OPIC-1.0\ParameterSet\Pset_Source_System'
$psetPath = 'K:\Temp\edw-release-2017.W21\OPIC-1.0\ParameterSet\TD_GCFR_PS'

$fileList = Get-ChildItem -Path $psetPath -Filter *.*;

foreach ($file in $fileList)
{
    # $content = Get-Content -Path $file.FullName # -Raw
    $content = [System.IO.File]::ReadAllText($file.FullName) #.Replace($findString,$replaceString)

    foreach( $token in $tokenList.GetEnumerator() )
    {
        $pattern = '{0}' -f $token.key
        $content = $content -replace $pattern, $token.Value
    }

    Write-Host $file.FullName
    #$outputFile = Join-Path -Path 'c:\windows' -ChildPath $folder
    $outputFile = '{0}\{1}' -f $file.Directory, $file.BaseName + '_TEST' + $file.Extension;
    Set-Content -Path $outputFile -Value $content;
 
    #$content
}
Write-Host 'Finished!'