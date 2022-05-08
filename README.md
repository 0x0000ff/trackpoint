# trackpoint
Build for use with my Thinkpad T440p, but maybe it can be used with other laptops with a Synaptics trackpoint. Made to work with newer Linux systems

## Install

```sh
git clone https://github.com/0x0000ff/trackpoint.git
```

```sh
cd trackpoint
```

(as root)

```sh
groupadd -f trackpoint
```

```sh
usermod -aG trackpoint $USER
```

```sh
make install
```

