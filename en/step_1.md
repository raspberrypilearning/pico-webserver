# Serve a webpage from your Pico 2 W

## Connect your Raspberry Pi Pico

Connect your Raspberry Pi Pico to your computer, and access it using Thonny. [You can follow the instructions in this project if you need guidance.](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0)

## Project files

Download these project files:

- [main.py](resources/main.py)
- [index.html](resources/index.html)

## Create `secrets.py`

> [!TASK]
>
> In Thonny, create a new file called `secrets.py`.
>
> Add your Wi-Fi name and password:
>
> ```python
> WIFI_SSID = "YOUR_WIFI_NAME"
> WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
> ```

> [!TASK]
>
> Save the `secrets.py` file **to the Pico**.
>
> ![Thonny showing a new file called secrets.py with Wi-Fi credentials entered and the save-to-Pico option selected](images/create-secrets-py.png)

## Upload `main.py`

> [!TASK]
>
> Open the downloaded `main.py` in Thonny.
>
> Save it **to the Pico** as `main.py`.
>
> ![Thonny showing the downloaded main.py file open and being saved to the Raspberry Pi Pico 2 W](images/upload-main-py.png)

## Upload `index.html`

> [!TASK]
>
> Open the downloaded `index.html`. You may have to change the file filter in Thonny to allow **all files** to be opened.
>
> ![File chooser with the Filter menu set to all files (*) so index.html is selectable](images/change-file-filter.png)

> [!TASK]
>
> Save the `index.html` **to the Pico**, and when prompted for a filename, **right-click** to create a new directory.
>
> ![The Save to Raspberry Pi Pico dialog in Thonny with the New directory option selected](images/new-directory.png)
>
> Call the new directory `www` and save the `index.html` file there.
>
> ![The Raspberry Pi Pico 2 W file system in Thonny with a new folder called www being created](images/create-www-folder.png)
>
> ![The Save to Raspberry Pi Pico dialog in Thonny showing the www folder open and index.html entered as the file name](images/save-index-to-www.png)

## Run the web server

> [!TASK]
>
> Go back to `main.py` and click **Run** in Thonny.
>
> If your Pico connects to Wi-Fi, it will print an IP address in the Shell.
>
> It will look something like this:
>
> ```text
> Open http://192.168.0.45/
> ```
>
> Make a note of the address.
>
> ![The Thonny Shell showing the Pico 2 W printing its IP address after connecting to Wi-Fi](images/pico-ip-address-in-shell.png)

## Open the page

> [!TASK]
>
> Make sure the computer or phone you are using is on the same Wi-Fi network as the Pico.
>
> Type the Pico's IP address into a web browser.
>
> You should see your web page.
>
> ![A browser on the local network displaying the simple Pico web page](images/browser-showing-pico-page.png)

## Change the page

> [!TASK]
>
> Open `www/index.html` on the Pico in Thonny.
>
> Change the text in the page, then save the file and refresh the browser.
>
> For example, you could change the heading and paragraph to something else.
>
> ![Thonny showing index.html open for editing, with the browser beside it displaying the updated page](images/edit-index-html-and-refresh.png)

## Test without Thonny

> [!TASK]
>
> Disconnect the Pico from Thonny.
>
> Power it from USB using a normal power supply.
>
> Wait a few seconds for it to start, then visit the same IP address again.
>
> Your web page should still load.
>
> ![A Raspberry Pi Pico 2 W powered from USB without a computer, serving the page to another device on the network](images/pico-powered-without-computer.png)
