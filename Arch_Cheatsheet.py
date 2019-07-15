# Arch Linux CheatSheet
print('''
                        ~गोबिंद झा(GitHub: jha-git)
    _    ____   ____ _   _   _     ___ _   _ _   ___  __
   / \  |  _ \ / ___| | | | | |   |_ _| \ | | | | \ \/ /
  / _ \ | |_) | |   | |_| | | |    | ||  \| | | | |\  /
 / ___ \|  _ <| |___|  _  | | |___ | || |\  | |_| |/  \

/_/   \_\_| \_\\_____|_| |_| |_____|___|_| \_|\___//_/\_\

                  ____ _   _ _____    _  _____   ____  _   _ _____ _____ _____
                 / ___| | | | ____|  / \|_   _| / ___|| | | | ____| ____|_   _|
                | |   | |_| |  _|   / _ \ | |   \___ \| |_| |  _| |  _|   | |
                | |___|  _  | |___ / ___ \| |    ___) |  _  | |___| |___  | |
                 \____|_| |_|_____/_/   \_\_|   |____/|_| |_|_____|_____| |_|''' )




ch = 'N'
while (ch == 'N' or ch == 'n' or query_no !=0):

    print("_________________________________MAIN MENU:___________________________________")
    print('''
             1. Access Rights
             2. Files and Directories
             3. Network
             4. System and Screen
             5. Package Management
             0. Exit''' )
    print("______________________________________________________________________________")
    query_no=int(input("Enter Your Query:"))


    if query_no==1:
        print('''
    _                           ____  _       _     _
   / \   ___ ___ ___  ___ ___  |  _ \(_) __ _| |__ | |_
  / _ \ / __/ __/ _ \/ __/ __| | |_) | |/ _` | '_ \| __|
 / ___ \ (_| (_|  __/\__ \__ \ |  _ <| | (_| | | | | |_
/_/   \_\___\___\___||___/___/ |_| \_\_|\__, |_| |_|\__|
                                        |___/

        ''')
        print('''
    sudo command                # executes command as root
    sudo -k                     # empties password cache
    sudo visudo                 # edits /etc/sudoers
    passwd                      # changes user password
    chown owner:group           # changes owner and group of file
    chmod permissions file      # changes the file permissions
                                to set permissions in octal mode:
                                4 (read) 2 (write) 1 (execute)
                                example - 755 read-write-execute for owner
                                amd read-execute for group and others
    ls -lh [dir]                # displays files and permissions [of directory]
            [use man command for more information]
         ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'

    elif  query_no==2:
        print('''
  ____ _ _                             _
|  ___(_) | ___  ___    __ _ _ __   __| |
| |_  | | |/ _ \/ __|  / _` | '_ \ / _` |
|  _| | | |  __/\__ \ | (_| | | | | (_| |
|_|   |_|_|\___||___/  \__,_|_| |_|\__,_|

 ____  _               _             _
|  _ \(_)_ __ ___  ___| |_ ___  _ __(_) ___  ___
| | | | | '__/ _ \/ __| __/ _ \| '__| |/ _ \/ __|
| |_| | | | |  __/ (__| || (_) | |  | |  __/\__ \

|____/|_|_|  \___|\___|\__\___/|_|  |_|\___||___/
''')
        print('''
    cd dir                          # changes the working directory
    cd ..                           # changes to the parent directory
    ls                              # lists directory contents
    ls -a                           # also lists the hidden files
    cp target file                  # copies the file
    cp -r target directory          # copies the directory
    mv target source                # move/rename target source
    rm -r dir                       # removes directory recursively
    ln -s file link                 # removes directory recursively
    mount -t type dev path          # mounts file system
    mount -o loop iso path          # mounts iso image
    /home/user                      # home directory of user
    /etc                            # directory with global configurations
            [use man command for more information]
        ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'


    elif  query_no==3:
        print('''
 _   _      _                      _
| \ | | ___| |___      _____  _ __| | __
|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |\  |  __/ |_ \ V  V / (_) | |  |   <
|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
        ''')
        print('''
    ifconfig                        # displays network information
    iwconfig                        # displays wireless network information
    iwlist scan                     # lists wireless access points
    /etc/rd.d/network ifup interface
    /etc/rd.d/network ifdown interface
    /etc/rd.d/iptables {start|stop|restart}
    ufw enable                      # enables the firewall [package Community: ufw]
    ufw default allow/deny          # allows/denies all incoming traffic
    ufw status                      # displays firewall status and rules
    ufw allow/deny port             # allows/denies incoming traffic on the specified port
    ufw allow/deny from ip          # allows/denies incoming traffic from specified IP address
            [use man command for more information]
            ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'



    elif  query_no==4:
        print('''
 ____            _                                   _
/ ___| _   _ ___| |_ ___ _ __ ___     __ _ _ __   __| |
\___ \| | | / __| __/ _ \ '_ ` _ \   / _` | '_ \ / _` |
 ___) | |_| \__ \ ||  __/ | | | | | | (_| | | | | (_| |
|____/ \__, |___/\__\___|_| |_| |_|  \__,_|_| |_|\__,_|
       |___/
 ____
/ ___|  ___ _ __ ___  ___ _ __
\___ \ / __| '__/ _ \/ _ \ '_ \

 ___) | (__| | |  __/  __/ | | |
|____/ \___|_|  \___|\___|_| |_|

            ''')
        print('''
    uname -r                    # displays the kernel version
    uname -a                    # displays all the kernel versiondf # reports file system disk space usage
    top                         # displays system tasks
    procinfo                    # displays system information [package Core:procinfo-ng]
    pstree                      # display a tree of processes
    Ctrl+Alt+Fn                 # switches to tty n
    Ctrl+Alt+F7                 # switches to the X session
    rc.d start daemon           # starts a daemon
    rc.d stop daemon            # stops a daemon
    rc.d restart daemon         #restarts a daemon
    shutdown -h now             # shuts the sytem down
    shutdown -r now             # restarts the system
    [use man command for more information]
            ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'



    elif  query_no==5:
        print('''
 ____            _
|  _ \ __ _  ___| | ____ _  __ _  ___
| |_) / _` |/ __| |/ / _` |/ _` |/ _ \

|  __/ (_| | (__|   < (_| | (_| |  __/
|_|   \__,_|\___|_|\_\__,_|\__, |\___|
                           |___/
 __  __                                                   _
|  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
| |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                          |___/

            ''')
        print('''
    pacman -Si pckg         # shows package information
    pacman - S pckg         # installs a package
    pacman -Rns pckg        # removes a package, its dependencies and configuration files
    pacman -Syu             # complete package upgrade
    pacman -Ss name         # searches for packages
    pacman -Q pckg          # diplays installed packages
    pacman -Ql pckg         # lists all package files
    pacman -U pckg.tar.xz   # installs a package from a file
    pacman -Qm              # lists manually installed packages
    yaourt -S pckg          # installs a package from AUR [package AUR: yaourt]
    yaourt -Syua            # complete package upgrade including packages from AUR

    man pacman.conf/makepkg # learn more about pacman
    * use pacman as root or with sudo
    use yaourt as non-privileged user
            ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'


    elif query_no == 0:
       exit()
