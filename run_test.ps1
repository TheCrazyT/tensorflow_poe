Set-Item -Path Env:Path -Value ("C:\Python36-x64\Scripts;c:\Python36-x64;" + $Env:Path)
echo $ENV:PATH
& dir c:\
& dir
& python --version
& python -c "import platform;print(platform.architecture())"
& python -c "import platform;print(platform.machine())"
& python -c "import platform;print(platform.python_compiler())"
& python -c "import platform;print(platform.python_implementation())"
& python -c "import pip._vendor.distlib.wheel as wh;print(wh.COMPATIBLE_TAGS)"
& python -m pip install wheel
& python -m pip install tf-nightly

#& python -m pip install tensorflow
#& python -m pip install tensorboard

& echo !!!!!!!!now starting tensorboard!!!!!!!!
start "C:\Python36-x64\Scripts\tensorboard.exe" -ArgumentList '--logdir checkpoints'
Start-Sleep -s 5
start "c:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -ArgumentList "http://localhost:6006"
#Start-Process -NoNewWindow -FilePath "C:\Python36-x64\Scripts\tensorboard.exe" -ArgumentList "--logdir checkpoints"

& echo !!!!!!!!now starting sample tensorflow script!!!!!!!!
& python doit.py
if ($LastExitCode -ne 0) { $host.SetShouldExit($LastExitCode)  }
