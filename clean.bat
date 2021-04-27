@echo off
del /Q /F .\*.wav .\*.mp3 .\*.m4a .\*.opus .\*.ogg .\*.flac 2>nul
rmdir /S /Q .\build 2>nul
rmdir /S /Q .\dist 2>nul
del /S /Q .\splits\* 2>nul
del /Q /F *.webm.part 2>nul
del /Q /F .\__pycache__ .\utils\__pycache__ .\MetadataProviders\__pycache__ 2>nul

