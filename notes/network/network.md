## Network

### Network Layers - Open Systems Interconnection model (OSI model)


| Layer           | Protocol data unit  | Function |
|-----------------| ------------------- | ---------|
|Application      | Data                | High-level APIs, including resource sharing, remote file access. <br /> 它是用户应用程序和网络之间的接口，完成用户希望在网络上完成的各种工作。它在其他六层工作的基础上，负责完成网络应用程序与网络操作系统之间的联系。应用层为用户提供的常见服务有文件服务、目录服务、文件传输服务（FTP）、远程登录服务（Telnet）、电子邮件服务（E-Mail）、打印服务、安全服务、网络管理服务、数据库服务等。|
|Presentation     | Data                | Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption. <br /> 它的主要功能是协商和建立数据交换的格式，解决各应用程序之间在数据格式表示上的差异,，以使一个主机应用层的数据可以被另一个主机的应用层理解，如数据的加密、解密、编码、格式转换等。 |
| Session         | Data                | Managing communication sessions, i.e., continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes. <br /> 这一层又称会晤层或对话层，其主要任务是负责维护两个实体之间的会话连接确保点到点的传输不被中断，并进行会话管理和数据交换管理，即组织和协调两个会话进程之间的通信，并对数据交换进行管理。 |
| Transport       | Segment, Datagram   | Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing. <br /> OSI下三层的主要任务是数据通信，上三层的任务是数据处理。因此，该层是通信子网和资源子网的接口和桥梁，起到了承上启下的作用。该层提供会话层和网络层之间的传输服务，这种服务从会话层获得数据，并在必要时对数据进行分割然后将数据传递到网络层，并确保数据能正确无误地传送到网络层。因此,运输层负责提供主机中两个进程之间数据的可靠传送。运输层的目的是向用户透明地传送报文，它向高层屏蔽了下层数据通信的细节。运输层的数据传输单元是报文段（segment），简称报文。该层协议的代表包括TCP、UDP、SPX等. |
|Network          | Packet              | Structuring and managing a multi-node network, including addressing, routing and traffic control.<br />  网络层的主要任务是为网络上的不同主机提供通信。它通过路由选择算法，为分组通过通信子网选择最适当的路径，以实现网络的互连功能。具体地说，数据链路层的数据在这一层被转换为数据包，然后通过路径选择、分段组合、流量控制、拥塞控制等将信息从一台网络设备传送到另一台网络设备。网络层负责在网络中传送的数据单元是分组或包。该层协议的代表包括IP、IPX、RIP、OSPF等 |
|Data link        | Frame               | Reliable transmission of data frames between two nodes connected by a physical layer.<br /> 它的主要任务是负责在两个相邻结点之间的线路上无差错地传输以帧为单位的数据，即将一条有可能出差错的实际链路转变成让网络层向下看去好像是一条不出差错的链路。数据链路层将数据分解成帧，然后按顺序传输帧，每一帧包括数据和必要的控制信息（包括同步信息、地址信息、差错控制信息和流量控制信息等）。该层协议的代表包括SDLC、HDLC、PPP、STP、帧中继等 |
|Physical         | Bit, Symbol         | Transmission and reception of raw bit streams over a physical medium.<br /> 物理层的任务是透明地传送比特流。现有计算机网络中的物理设备和传输媒体种类繁多，通信手段也有多种，物理层的作用正是要尽可能地屏蔽这些差异，使物理层上面的数据链路层感觉不到这些差异。该层的典型规范代表包括：EIA/TIA RS-232、EIA/TIA RS-449、V.35、RJ-45等 |


### TCP 可靠传输

* 三次握手，保持两端建立连接
* 对数据编号，保证有序发送，接收端有可能需要进行排序保证接受的数据有序
* 接收端丢弃重复序列号重复数据。
* 确认应答， 接收端每次接收到数据后，都对传输端确认应答（ACK）。
* 校验和。首部和数据校验和，确保数据传输过程中没有任何变化。如果校验和出错，则不确认收到此报文。
* 超时重传。当 TCP 发出一个段后，它启动一个定时器，等待目的端确认收到这个报文段。如果不能及时收到一个确认，将重发这个报文段。
* 流量控制。在TCP协议的报头信息当中，有一个16位字段的窗口大小， 接收端会在确认应答发送ACK报文时，将自己的即时窗口大小填入，并跟随ACK报文一起发送过去。而发送方根据ACK报文里的窗口大小的值的改变进而改变自己的发送速度。如果接收到窗口大小的值为0，那么发送方将停止发送数据。并定期的向接收端发送窗口探测数据段，让接收端把窗口大小告诉发送端。
* 拥塞控制。当网络拥塞时，减少数据的发送。

