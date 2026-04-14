# Implementation and Analysis of QoS Simple Priority Controller in Software Defined Networking using Mininet and POX Controller

---

## 1. Introduction

Software Defined Networking (SDN) is a modern networking approach where the control plane is separated from the data plane. This allows centralized control and programmability of the network.

Quality of Service (QoS) is used to prioritize network traffic so that critical applications get better performance.

In this project, we implemented a **Simple Priority-Based QoS Controller** using POX and simulated the network using Mininet.

---

## 2. Objectives

- Design SDN topology using Mininet  
- Implement QoS controller using POX  
- Generate ICMP, HTTP, and TCP traffic  
- Analyze behavior under congestion  
- Validate results using Wireshark  

---

## 3. Tools & Technologies

- Mininet  
- POX Controller  
- Python  
- Wireshark  
- iperf  
- Ubuntu Linux  

---

## 4. System Setup

### 4.1 Update System

```bash
sudo apt update
sudo apt upgrade
