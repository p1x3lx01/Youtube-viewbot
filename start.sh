#!/bin/bash

# تثبيت Google Chrome
echo "تحميل Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

echo "تثبيت Google Chrome..."
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install

# تحديد الإصدار الكامل لـ Google Chrome
CHROME_VERSION_FULL=$(google-chrome --version | cut -f 3 -d ' ' | cut -d '.' -f 1,2,3)
echo "إصدار Google Chrome الكامل: $CHROME_VERSION_FULL"

# إزالة ChromeDriver القديم إن وجد
echo "إزالة ChromeDriver القديم إن وجد..."
sudo rm -f /usr/local/bin/chromedriver

#!/bin/bash

# تحديد رابط تحميل ChromeDriver
CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.159/linux64/chrome-linux64.zip"

# إزالة ChromeDriver القديم إن وجد
echo "إزالة ChromeDriver القديم إن وجد..."
sudo rm -f /usr/local/bin/chromedriver

# تحميل ChromeDriver
echo "تحميل ChromeDriver من $CHROMEDRIVER_URL ..."
wget "$CHROMEDRIVER_URL" -O chromedriver_linux64.zip

# تثبيت ChromeDriver
echo "تثبيت ChromeDriver..."
unzip -o chromedriver_linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver

echo "تم تثبيت ChromeDriver بنجاح."
