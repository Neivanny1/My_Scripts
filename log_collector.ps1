# Get all Wi-Fi profiles
$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_ -replace "^\s+|\s+$" }

# Save Wi-Fi names and passwords to a file
foreach ($profile in $wifiProfiles) {
    $wifiName = $profile -replace "All User Profile\s+:\s+"
    $password = (netsh wlan show profile name="$wifiName" key=clear | Select-String "Key Content").ToString() -replace "Key Content\s+:\s+"

    # Save to a file
    Add-Content -Path "File.txt" -Value "Wi-Fi Network: $wifiName, Password: $password"
}

#incase script failes open powershell as administrator and run
set-executionpolicy remotesigned
