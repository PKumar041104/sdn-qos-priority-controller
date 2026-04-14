# Implementation and Analysis of QoS Simple Priority Controller in Software Defined Networking using Mininet and POX Controller

## Department of CSE, PES University  
**Course:** Computer Networks  
**Project Type:** SDN Mininet Project  
**Student Name:** Pratham Kumar  
**SRN No.:** PES2UG24CS368  
**PRN No.:** PES2202400086  

---

## 1. Project Overview

This project presents the implementation and analysis of a **QoS Simple Priority Controller** in a Software Defined Networking environment using **Mininet** and the **POX Controller**. The main purpose of the project is to understand how an SDN controller can centrally observe traffic, classify it into different priority levels, and analyze network behavior under single-flow and multi-flow conditions.

Traditional networks tightly couple the control plane and data plane inside networking devices. In contrast, SDN separates these two functions. The forwarding devices mainly handle packet forwarding, while the controller makes decisions about network behavior. This separation makes the network programmable, flexible, and easier to manage. In this project, that SDN concept is explored through a simulated network in Mininet and a controller implemented in POX. 

The project specifically focuses on **Quality of Service (QoS)** using a simple priority-based approach. Different traffic types were treated as different priority classes. ICMP traffic was treated as high priority, HTTP traffic as medium priority, and bulk TCP traffic generated using iPerf as low priority. The behavior of these traffic flows was observed both individually and under simultaneous contention through a bottleneck switch. This allowed us to study latency-sensitive traffic, application traffic, and bulk transfer traffic in a controlled SDN setup. 

---

## 2. Introduction to SDN

Software Defined Networking is a networking paradigm in which the intelligence of the network is moved from distributed devices into a logically centralized controller. This controller communicates with switches using protocols such as OpenFlow and can dynamically influence forwarding behavior. SDN is important because it enables programmability, centralized monitoring, policy enforcement, traffic engineering, and easier experimentation.

In a conventional network, each switch or router independently makes forwarding decisions using locally stored rules. In SDN, the controller has a global view of the network and can react to network events such as new flows, congestion, failures, or policy violations. This is especially useful when implementing traffic classification, access control, routing policies, and QoS behavior.

In this project, POX acts as the SDN controller and Mininet acts as the virtual network emulator. POX receives `PacketIn` events from switches, inspects the incoming traffic, and classifies it into different priority levels. Mininet provides hosts, switches, and links in software, allowing the entire experiment to be performed on a single Ubuntu virtual machine. 

---

## 3. Introduction to QoS and Priority Scheduling

Quality of Service refers to the ability of a network to treat traffic differently depending on its importance and performance requirements. Not all traffic has the same needs. Some traffic, such as control messages or interactive communication, is more sensitive to delay. Other traffic, such as file transfer or bulk data transfer, can tolerate more delay.

A priority-based QoS model assigns different preference levels to different traffic classes. In a simple priority controller:

- high-priority traffic should receive faster and more reliable handling,
- medium-priority traffic should receive moderate preference,
- low-priority traffic should still be served, but can tolerate more competition and delay.

This project demonstrates that idea in an SDN setting by observing three traffic types:
- **ICMP** for high-priority traffic,
- **HTTP on port 8080** for medium-priority traffic,
- **bulk TCP on port 5001** using iPerf for low-priority traffic.

The emphasis of the project is not on industrial-grade queue scheduling, but on the SDN-side classification, observation, and analysis of traffic behavior under bottleneck conditions. 

---

## 4. Problem Statement

The goal of this project is to implement an SDN-based solution using Mininet and an OpenFlow controller, demonstrating:

- controller-switch interaction,
- packet classification logic,
- handling of `PacketIn` events,
- flow behavior under different traffic conditions,
- performance observation using tools such as Wireshark, ping, HTTP, and iPerf.

The project also aims to validate network behavior under different scenarios and provide proof through screenshots, logs, and reports. The faculty requirements explicitly emphasized topology creation, controller logic, observable scenarios, proof of execution, and GitHub documentation. :contentReference[oaicite:6]{index=6}

---

## 5. Objectives

The objectives of this project are:

1. To understand the SDN model and the separation of control plane and data plane.
2. To create a custom Mininet topology representing a bottleneck-based network.
3. To implement a POX controller capable of handling `PacketIn` events.
4. To classify traffic into high, medium, and low priority categories.
5. To generate and analyze ICMP, HTTP, and TCP bulk traffic.
6. To study single-flow and mixed-flow behavior through a bottleneck switch.
7. To verify traffic at the packet level using Wireshark.
8. To document the entire process in a professional and reproducible way. 

---

## 6. Tools and Technologies Used

The following tools and technologies were used in this project:

- **Ubuntu Linux VM** as the working environment
- **Mininet** for SDN network emulation
- **POX Controller** for SDN control logic
- **Python** for writing topology and controller code
- **Wireshark** for packet capture and analysis
- **ping** for ICMP traffic generation and latency observation
- **Python HTTP Server** for application-layer web traffic
- **iPerf / iPerf3** for bulk TCP traffic generation
- **Git and GitHub** for version control and final project submission

These tools collectively allowed both implementation and validation of the project. 

---

## 7. System Preparation and Installation

### 7.1 Updating the Ubuntu VM

Before starting Mininet and POX setup, the Ubuntu virtual machine was updated so that packages, dependencies, and system libraries were current.

```bash
sudo apt update
sudo apt upgrade -y
```

This step is important because dependency issues often arise in older or partially updated installations. The Mininet installation guide also begins with system update commands for this reason.

---

### 7.2 Installing Mininet

Mininet was installed using Ubuntu’s package manager:

```bash
sudo apt install mininet -y
```

This installs Mininet, Open vSwitch, and the required dependencies needed for virtual hosts, switches, and links. The installation manual provided for the course also recommends direct installation through the package manager as the simpler and recommended method.

---

### 7.3 Verifying Mininet Installation

Mininet can be verified using:

```bash
sudo mn
```

Inside the Mininet CLI:

```bash
pingall
```

A correct installation should show successful host-to-host communication with no packet loss. The course installation document lists this as the standard verification method.

---

### 7.4 Obtaining POX Controller

POX was used as the SDN controller for this project. The controller code was placed in the ext directory of the POX repository so that it could be loaded as a custom POX module.

---

## 8. Project Title Explanation
