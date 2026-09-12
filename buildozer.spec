name: Build Android APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build with Buildozer
        uses: kivy/buildozer-action@master
        id: buildozer
        with:
          command: buildozer -v android debug
          
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: bin/*.apk