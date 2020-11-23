# Basics

- Department can have hierarchical structure (partent department)
- If create employee from department, the department field is automatically filled
- Work Address and Work Location
- The manager of the department will be auto filled for the manager, time off responsible, expense responsible, coach
- When u save the creation of employee, organization chart will appear (show organization chart enable in settings)
- Add a related user in HR Settings tab: the related user will be the database user
- Can choose who to send appraisal form to: manager, employee, collaborator, colleagure
- Timesheet cost per hour
- Upload files to personal document tab
- Set working time in settings
- By clicking on Work Resources button on Company Working Hours: it shows all employees that have that working hours

- Groups in Employee:
  - Kiosk Attendance: able to open the kiosk mode and validate the employee pin
  - Officer: able to approve document created by employee
  - Administrator: have access to hr configuration + static report



# Attendance

- Enable Employee PIN
- Add pin/badge in HR Settings tab in employee template
- Print badge by (from action gear)
- To check in/out by badge or PIN, use Manage Attendace > Kiosk mode
- Groups:
  - Manual Attendance: access to hr attendance menu, manage his own attendance
  -

# Time Off

- Define the kinds of Time Off Type
  - No Allocation is need: employee can take as they want
  - Free to request
  - allocated by hr only
  - Responsible field is required
  - validity date
  - Edit work entry type:
    - define how it is displayed in the payslip
- To create time off allocation, go to manager > allocations
  - Required: mode (by employee/department/company), description, time off type
- When allocation is approved, can request a time off
- On the top of dashboard we can see the days left we can take or the time off we ve taken
- Can click `Create a time off request` or just click on the day on calendar
- To approve time off: Manager > Time Off, the default filter let u see only request of employees you manage
- You can see who else has taken days off within this month
- To looking at everyone time off: click on everyone menu

# Appraisal

- Settings: min/max time btw appraisal req, reminder (auto send remind email),
- Set appraisal reminder required:
  - who to notify
  - when
  - subject
- Default participant
- Change the default email send to participants
- Can request new appraisal from Appraisal app and Employee (Employee template) as well
- the appraisal request requires desired deadline
- Appraisal:
  - add many managers, subordinates, colleagues
  - When confirm and send from , state changes to appraisal send
- Reporting:
  - Gantt view:
    - Rows: department (change in group by)
    - cols: time

# Skill Management

- Enable in settings
- Resume:
  - Different type of skill: experiece, education, internship...
  - Display types: classic, cert, course
  - start-end date
  - Each type is a section in resume

- Skill
  - type: language, dev, music,...

- Can search employee by skill (search skill for / search resume for)

# Recruitment

- Create job position from dashboard view or config > job postions
- Job position:
  - only thing required is name of the job
  - 3 dots > Recruitment done
  - Published banner
  - To publish, go to website and edit webpage
  - publish webpage by button on the top bar
  - the name of responsible person is in grey and below the job position, above the button
- Applications:
  - change state to first interview: auto send notif email
  - If we set up the recruitment form, when press start interview, the form show up (enable Interview Form in settings)
  - can print interview (the survey form) in application template
  - Create offer link
  - When she accept the offer, move from contract proposal to contract sign, create employee

# Referrals

- customize level
- customize onboarding mess, alert

# Expenses

- Create expense from incoming email (enable in settings)
- Product has option `Can be expense`
- Internal Reference: Use this reference as a subject prefix when submitting by email
- New Expenses:
  - Reinvoice Customer: Let’s take the example of an consultant paying an hotel to work on the site of your client. As a company, you would like to be able to invoice that expense to your client.
  - For all expenses, we can attach documents
- Can group multiple expenses to create report
- To have the list of all report to approve: Expense Report > To Approve
- Can reimburse (register a payment) employee once the journal entry is posted (after approved)
- Can set time range in expenses report

# Payroll

- warning sign: they dont have any running contracts or expired
- Contract:
  - HR Responsible: person responsible for validating the employee contract
  - New Contract Document Template: default document that the applicant will have to sign to accept a contract offer
  - Contract Update Document Template: default document that the employee will have to sign to update his contract
  - Contract Detail;
    - Salary Structure Type, Working Schedule are required
  - Salary Information
    - Wage Type
    - Wage Amount
    - Can add IP percentage
    - Fiscal Voluntarism: Voluntarily increase withholding tax rate
    - Commission on target: monthly gross amount that the employee receives if the target is reached
  - For part-time worker, use credit time button
  - Can generate simulation link: it sends the contract to the employee to sign
  - Can configure some additional advantages (order new car ...)


- How much we pay for the employees base on Work Entries
- Need to validate entries before generate payslip
- Wont be able to generate payslip if there are conflicts with our work entries (little orage flag on the work entry or going to work entry > conflict)
- Can create payslip by batch
- By Clicking on `Create Draft Entry`, it will post some entries to accounting application (if you enable Payroll entries in settings)
- Salary Rules are created based on your fiscal localisation, but you can create your rules
-
