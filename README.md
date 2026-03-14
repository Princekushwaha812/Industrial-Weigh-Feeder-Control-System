# Industrial-Weigh-Feeder-Control-System
Monitoring and control logic for industrial weigh feeders using load cells, tachometers, and VFD frequency modulation.

# Industrial Weigh Feeder Monitoring & Control System

### **Project Overview**

This project documents the design and operational logic of an industrial **Weigh Feeder**, a critical instrument used in cement, steel, and mining industries. The system provides controlled and continuous feeding of raw materials by integrating real-time weight and speed data to ensure a consistent flow rate for downstream processes.

### **System Architecture & Hardware**

The system relies on a closed-loop feedback mechanism involving the following core elements:

* **Conveyor Belt**: The primary medium for material transport.


* **Load Cell**: A transducer mounted beneath the frame that converts the force of the material into an electrical signal using the strain gauge principle.


* **Tachometer**: Measures the rotational speed (RPM) of the drive or tail pulley to determine belt velocity.


* **PLC/Controller**: The central processing unit that calculates the mass flow rate (TPH).


* **Variable Frequency Drive (VFD)**: Adjusts motor speed based on feedback to maintain the target feed rate.



### **Technical Logic & Mathematical Modeling**

To be "High-Paying Job Ready," the system must execute the following calculations with 100% accuracy:

#### **1. Flow Rate Calculation (TPH)**

The Tons Per Hour (TPH) is derived from the belt load and belt speed:


$$TPH = \text{Belt Load (kg/m)} \times \text{Belt Speed (m/s)} \times 3.6$$



* 
**Example**: At a load of 100 kg/m and a speed of 1.2 m/s, the system outputs **432 TPH**.



#### **2. Signal Processing (4-20 mA Mapping)**

The TPH value is converted into an industry-standard 4-20 mA analog signal for communication with the DCS:


$$\text{Output Current (mA)} = 4 + \left( \frac{\text{Current TPH}}{\text{Max TPH}} \right) \times 16$$



* 
**Example**: For a 350 TPH current flow against a 500 TPH maximum, the signal is **15.2 mA**.



#### **3. Flow Rate Control (VFD Modulation)**

When the target TPH changes, the VFD modifies the motor frequency:


$$\text{New Frequency} = \text{Current Frequency} \times \left( \frac{\text{Target TPH}}{\text{Current TPH}} \right)$$



### **Key Learnings**

* Applied Wheatstone bridge circuit theory for load measurement.


* Mastered pulse frequency analysis for speed detection.


* Implemented 4-20 mA signal loop mapping for industrial automation.
