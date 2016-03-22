Workload based assessment allegedly allows for independent analysis that creates a model for work activity to be used for future hiring.

"We demonstrate how to conduct a workload-based assessment by examining the distribution of calls for service in four law enforcement agencies" (pg 36)

###The Process

Process outlined as (page 36):

```
There are six steps in this process:
•	Examine the distribution of calls for service by hour of day, day of week, and month
•	Examine the nature of calls for service
•	Estimate time consumed on calls for service
•	Calculate agency shift-relief factor
•	Establish performance objectives
•	Provide staffing estimates
```

Provides estimate for patrol division

###Step by Step

# Examine the distribution of calls for service by hour of day, day of week, and month

# Examine the nature of calls for service

# Estimate time consumed on calls for service

# Calculate agency shift-relief factor

Table 3.5 & 3.6 outline this approach (page 42)

```
work_hours = (Days a year * length of shift)

shift_size = work_hours / (work_hours - total_time_off)
```

Total time off can be calculated by:
* Finding data noted about how time off used
* Assuming officers will use max time off opps (e.g. if given 10 sick days an officer will use all of it)

Either of these will need to consider things such as "a shift with senior officers would have a higher  shift-relief factor than one  with junior officers. Adjusting  for this difference makes the  workforce model more reliable" as senior officers have more time off options 

Total number of offices needed for a day:

```
shifts_per_day = hours_day / length_shift
total_officers_day = shifts_per_day * shift_size
```

# Establish performance objectives

Goal: Determine what fraction of a shift devoted to calls for service and what portion goes to other activities

Their estimate based on known community made workload (calls for service) - easiest to measure and reflects demand for police service

"We believe that this approach is very reliable, because other activity categories are often duplicative." (pg 44)

"Noting the possible confusion of categories does not denigrate these activities. Rather, the point is that many police activities are discretionary." (pg 44)

"The community, through policy-makers, must then determine what fraction of an officer’s day should be available for other activities." (pg 45)

"Once the community sets a performance objective, we can estimate the number of officers required." (pg 45)

"One useful tool to determine the appropriate amount of discretionary time is to conduct interviews and focus groups with elected officials as well as representatives of neighborhood and business organizations." (pg 45)

# Provide staffing estimates

Step 1: What is the # of officers needed to answer calls for service (CFS)?

1. Calculate number of hours needed to staff CFPs PER shift for an agency:

"In order to compensate for the failure of the CAD to capture multiple officer dispatches, we add 25 percent to the number of calls per shift." (pg 45)

Table 3.8 - shows adjusted calls for service data
Table 3.9 - Est office time per CFS

num_hours_to_staff_cfs = modifed_num_calls * avg_time_call 

2. Determine how many officers needed per shift to staff CFS

hrs_officer_work_year = length_shift * 365

num_officers_staff_cfs = cfs_per_shift / hrs_officer_work_year

3. Examine performance objective

25% CFS
25% Patrol and Self-Initiated
25% Administrative
25% Criminal Investigation Follow-up

officers_per_shift = num_officers_staff_cfs * 4

Adjusting for number of days off an officer likely to take:

adjusted_officers_per_shift = officers_per_shift * shift_relief_factor

officers_per_day = adjusted_officers_per_shift * num_shifts_day

Step 2: Analyze patrol staffing in agency

1. Find CFS per shift:
	- removing traffic accidents
	- adjust CFS to include back up officer (total_cfs * percent_need_backup)
2. Find time devoted to calls
	- avg time for calls + avg time on scene
3. Est number of officers needed to handle these calls
	- num_officers_cfs = total_hrs_cfs / hrs_officer_per_year
	- hrs officer works a year based on shift length * 365 days
4. Use the time allocation of officer per shift to make estimate for number of officers needed 

	- Model 1: 50% CFS, 50% other
		- num_officers_cfs * 2
	- Model 2: 33% CFS, 33 admin, 33 officer led activities
		- num_officers_cfs * 3
	
	These models calculate number of officers needed for a shift

Table 3.18: Minimum Staffing Calculations for a Sample Chicago Police District, August 2008 to July 2009 (page 49)


###Limitations of the model

1. Relies heavily on avgs for making estimates
2. Model doesn't differentiate about job functions of police units
3. Response time as a part of CFS time - this may not be applicable in areas with large geographic zones
"In these agencies it is important to consider re-designing patrol zones to ensure that officers can respond to calls appropriately." (pg 51)
4. "inally, it is important to note that the workload-based approach works best when a community responds to at least 15,000 citizen-generated calls per year." (pg 51)

###TODO:

** Replicate table 3.18 for year by year
** Replicate table 3.15 for what is available vs. what is required
