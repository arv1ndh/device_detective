# **Device Detective** 


### 2nd Place for Best Tech  
### 3rd Place in Employers choice

**Executive Summary**

                 Alexandra Hussar       -- UI engineer

                 Arvindh Kumar Chandran -- Infrastructure engineer

                 Chad Bloxham           -- Cloud developer

**Background**

Many companies are now encouraging their employees to work using their own phones, computers, and other personal devices. This policy is known as &quot;Bring Your Own Device&quot; (BYOD), and it has numerous advantages. Reports indicate increased employee productivity and morale. It is also more convenient and makes companies seem more flexible and attractive to potential employees. Since much of modern work is done in the cloud as opposed to local machines, BYOD can be a cost-effective strategy for companies as well. Companies do not have to spend as much on IT personnel to manage the employee&#39;s devices, and many security functions can also be moved to the cloud.

**Product Description**

**Product Opportunity**

The flexibility of BYOD also brings with it a considerable amount of risk. Companies using this strategy must enforce certain security measures to make sure information doesn&#39;t fall in the wrong hands. One such use-case involves an employee using an insecure or old version of a web browser or operating system that can potentially be exploited by a malicious third-party which in turn can compromise the whole organization. It is important for organizations to know which software and devices employees are using. Knowing this information can improve not only the security, but also the proficiency of organizations. For example, this information can help inform the purchase of software which increases productivity and assists in regular business operations. It can also provide the organization with a better understanding of their employees, which will allow for the development of basic employee profiles.

**Product Vision**

We had two goals for our product. The first was to build a scalable and robust cloud system for processing http packets and extracting device information from them. The second was to create an application that queries the stored data and generates analytics which include a device profiling and potential vulnerabilities. From an employee&#39;s perspective, they should not feel any visible lag while using websites as it might hinder their work. From an employer&#39;s perspective, the application should display data in a fluid and dynamic manner across varied platforms for flexibility.

**Product Outcomes**

Our team started with a high level design of the architecture and the flow diagram. We developed a transparent proxy, that extracts essential headers from the http packets and sends them over the cloud for processing which was light weight and ensured low latency. All the services in cloud were chained and structured using a flow model which makes the system highly scalable and modular. The device profiling engine which forms the core of identification was chosen and evaluated among multiple choices by their accuracy and the information details. The UI was created on flutter, which made it cross-platform. By storing the data on firebase, it was coherent and we were able to get reports in real time. We also developed a company simulator program to test our prouct&#39;s scalability and accuracy.

**Product Deliverables**

Our deliverables are: (1) a transparent proxy which is able to intercept all the http packets and would be integrated into the company&#39;s gateway, (2) a cloud ecosystem that stores the parsed http header and user identification information and passes it to the device profiling engine for results, and (3) a user application that queries and generates reports based on the data received.

**Competitive Advantage**

Our product is lightweight and very easy to integrate. Having all of our core services over cloud ensures high resiliency, robustness and incredible scalability. Developing our app on flutter makes the user experience fluid, dynamic and gives the user the flexibility to view reports across various platforms.

**Financial Considerations**

We plan to offer a subscription based model that will scale with users. It will be priced per user per device for a company. The profit margins we seek ideally be around 50%, i.e we charge users twice of what we pay to keep our cloud services running.
