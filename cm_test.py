import pandas as pd

V_CM_ClientSummary = pd.read_csv("sample_data/sccm/V_CM_ClientSummary.csv")
print(V_CM_ClientSummary.head())
print(V_CM_ClientSummary.columns)
print(V_CM_ClientSummary['AADDeviceID']) # not entirely sure what this field is. but it is probably useful.

# see notes from meeting which sort of explain important fields:
"""
v_CH_ClientSummary		    by device	
ClientActiveStatus	        bool (1/0)		
ClientRemediationSuccess			
ClientState	                1 through 4		
ClientStateDescription			
ExpectedNextPolicyRequest			
IsActiveDDR			
IsActiveHW			
IsActivePolicyRequest			
IsActiveStatusMessages			
IsActiveSW	                actually communcating w server		
LastActiveTime			
LastDDR	when network hit		
LastEvaluationHealthy			
LastHealthEvaluation	    date of last		
LastHealthEvaluationResult	1 through 7 of how many passed from heath eval		
LastHW	                    last hardware scan		
LastMPServerName			
LastOnline	                full date object		
LastPolicyRequest	        checks into management point		
LastStatusMessage			
LastSW	                    last software scan		
ResourceID			
"""

V_R_System = pd.read_csv("sample_data/sccm/V_R_System.csv")
print(V_R_System.head())
print(V_R_System.columns)
print(V_R_System['Name0']) # according to notes, this is the active directory location?? use to pull from track-it
print(V_R_System['User_Name0']) # according to notes, this is the last person who logged on to the computer

# see notes from meeting on spreadsheet for vSMS_R_System. They show sort of what fields should be doing what.
# will paste them below for convenience:

"""
vSMS_R_System	{by device.	super important fields: resourceID - id per device; description0 - AD description}
Active0	                    1 or 0			
AD_Site_Name0				
AgentEdition0				
AlwaysInternet0				
AMTFullVersion0	            allows for remote control of computers.			
AMTStatus0	                status of AMT			
Build0				
Build01				
Client_Type0				
Client_Version0	            number build for the sccm client			
Client0	                    does it have sccm client or no			
Community_Name0				
CPUType0				
Creation_Date0	            date created			
Decommissioned0				
DeviceOwner0				
DiscArchKey				
Distinguished_Name0	        where located in AD			
EAS_DeviceID				
Full_Domain_Name0				
Hardware_ID0				
InternetEnabled0				
Is_AOAC_Capable0				
Is_Assigned_To_User0				
Is_MachineChanges_Persisted0				
Is_Portable_Operating_System0				
Is_Virtual_Machine0	        1 or 0	can use for filtering		
Is_Write_Filter_Capable0				
IsClientAMT30Compatible0				
IsReassigned0				
ItemKey				
Last_Logon_Timestamp0	    good stuff	is a time. In some format.		last logon0 is just the ms and use to subtract to compare
ManagementAuthority				
MDMStatus				
Name0	                    AD name	USE THIS TO PULL FROM TRACK-IT		
Netbios_Name0	            Actual hardcoded bios name			bios - chip at firmware level… might want to see discrepancies between name0 and this
Object_GUID0				
Obsolete0				
Operating_System_Name_and0  windows NT version		internal kernel that it exists on	
OSBranch0				
OSBranch01				
Previous_SMS_UUID0				
Primary_Group_ID0				
PublisherDeviceID				
Resource_Domain_OR_Workgr0				
rowversion				
SerialNumber				
SID0	                    letter number identifier for an AD object			
SMBIOS_GUID0				
SMS_Unique_Identifier0				
SMS_UUID_Change_Date0				
SuppressAutoProvision0				
Unknown0				
User_Account_Control0				
User_Domain0				
User_Name0	                AD name of person who last logged on	(see how long this stays the same person)
Virtual_Machine_Host_Name0				
Virtual_Machine_Type0				
WipeStatus0				
WTGUniqueKey				
IMEI				
AADTenantID				
MDMDeviceCategoryID0				
MDMStatusUpdatedTime				
AADDeviceID				
BuildExt				
DNSForestGuid
"""

