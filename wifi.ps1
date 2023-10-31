# Get a list of all saved Wi-Fi profiles
$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_ -replace "All User Profile\s+:\s+", "" }

# Loop through each Wi-Fi profile and retrieve the password
foreach ($profile in $wifiProfiles) {
    $result = (netsh wlan show profile name="$profile" key=clear)
    if ($result -ne $null) {
        $password = $result | Select-String "Key Content" | ForEach-Object { $_ -replace "Key Content\s+:\s+", "" }
        Write-Host "Wi-Fi Network: $profile"
        Write-Host "Password: $password"
    }
}
