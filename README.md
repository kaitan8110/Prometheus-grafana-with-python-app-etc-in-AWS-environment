In this documentation, i am going to detail the entire process of installing and configuring Prometheus, Grafana, and its related technologies in EC2 instances in AWS. 
We also have an example python app as well, to illustrate the instrumentation of python app, to expose its metrics to the prometheus server, so that prometheus can monitor it by scraping its metric on a regular interval. 

Without further ado, let's get started.. 

Let's look at the entire architecture diagram first. 
![Image description](doc_images/overall_architecture.png)

Below will list down the steps on how to configure the above architecture. 

Launch two EC2 instances in AWS. They can be in the same region and subnet. Use Amazon Linux AMI for your instances. For security group, create a new security group for each instance, and associate to each instance. The security groups should allow ssh access at port 22 from anywhere(0.0.0.0). We will configure as allow from any source first. We can then modify in future to only allow from certain ip/ ip range to enhance security.

Create a key pair in AWS. Save the private key with the .pem extension in your local environment. We will need to use it to ssh into our ec2 instances later. 

Create two EIPs and associate to your two vms. So that their public ip will not change everytime it is stop and start. 

Run the ssh command that is something like that to connect to your vm. Remember to replace the below content accordingly. 
```
ssh -i "<private_key_name>.pem" ec2-user@<replace_with_your_respective_public_dns>
```

We will then configure the VM1 first. By setting up Prometheus server --> Grafana --> Alertmanager --> Pushgateway --> Service Discovery.. 

Note that you may choose to skip or not set up any of the above software/tools. It should be based on your specific use case, and shouldn't be cast in stone.  

With that in mind, let's continue. 


- [Setup Prometheus Server](1_Set_up_Prometheus_Server.md)
- [Set_up_Grafana](2_Set_up_Grafana.md)
- [Set_up_Alertmanager](3_Set_up_Alertmanager.md)
- [Set_up_Pustgateway](4_Set_up_Pustgateway.md)
- [Set_up_Service_Discovery](5_Set_up_Service_Discovery.md)
- [Set_up_Node_exporter_in_VM2](6_Set_up_Node_exporter_in_VM2.md)
- [Set_up_Python_App](7_Set_up_Python_App.md)
- [Creating_a_Python_script_for_a_short_lived_job_and_push_its_metrics_to_Pushgateway](8_Creating_a_Python_script_for_a_short_lived_job_and_push_its_metrics_to_Pushgateway.md)
- [Set_up_monitoring_and_alerting_with_prometheus_n_alertmanager_via_gmail_email](9_Set_up_monitoring_and_alerting_with_prometheus_n_alertmanager_via_gmail_email.md)


That concludes our exploration of various technologies and tools available for monitoring and alerting, specifically focusing on Prometheus, Alertmanager, and their related technologies. The ability to continuously monitor our web architecture is crucial, as it enables us to proactively manage and maintain system performance. Additionally, alerting functions are vital; they ensure we are immediately notified and can promptly address any issues that deviate from the norm. The significance of these practices in maintaining efficient and reliable web services cannot be overstated. Thank you for reading.