# Updater for LeafPy. This will run and determine if there is a new version available. This file will be added to LeafPy on start up and prompt the user to update.

$latestVersion = cat < latest
$computerVersion = $1

if $latestVersion != $computerVersion then
  $input = echo "[y,n] A new version is available. Would you like to download it?"
  if $input == "y" then
    ./downloader.sh $latestVersion
fi
