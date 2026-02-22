# High Availability HPC Cluster

A robust High Availability (HA) High Performance Computing (HPC) Cluster designed to ensure continuous service availability, data integrity, and fault tolerance for mission-critical workloads using open-source Linux technologies.

---

## 📌 Overview

This project implements an HA Cluster architecture that provides automatic failover and seamless recovery in case of Master node failure. It leverages synchronous block-level replication, cluster resource management, centralized authentication, and job scheduling to support high-performance computing environments.

The solution eliminates single points of failure and guarantees uninterrupted access to computing and storage resources.

---

## 🏗️ Architecture

- Two Master Nodes (Active/Standby)
- Multiple Compute Nodes
- Shared Storage via DRBD + NFS
- Virtual IP managed by Pacemaker/Corosync
- Secure communication using WireGuard

---

## ⚙️ Technology Stack

- Operating System: Linux  
- Cluster Management: Pacemaker, Corosync, PCS  
- Data Replication: DRBD  
- Job Scheduler: Slurm  
- Authentication: LDAP  
- Shared Storage: NFS  
- Security: Iptables Firewall  
- VPN: WireGuard  
- Automation: Shell Scripting  

---

## 🔄 How It Works

1. DRBD mirrors data synchronously between Master and Standby nodes.  
2. Pacemaker continuously monitors node health.  
3. If the Master fails:  
   - Virtual IP moves to Standby node  
   - DRBD promotes Standby to Primary  
   - NFS, Slurm, and LDAP services restart automatically  
4. Users experience minimal or no downtime.

---

## 🚀 Features

- Automatic failover & recovery  
- Synchronous data replication  
- Centralized user authentication  
- Secure node-to-node communication  
- Scalable compute infrastructure  
- Firewall-protected environment  

---

## ✅ Verification

pcs status  
drbdadm status  
sinfo  
squeue  

---

## 📊 Use Cases

- Scientific computing  
- Machine learning workloads  
- Research clusters  
- Enterprise batch processing  

---

## 🔐 Security

- Only required ports are open via iptables  
- All cluster traffic encrypted using WireGuard  
- LDAP ensures centralized access control  

---

## 📜 License

MIT License
