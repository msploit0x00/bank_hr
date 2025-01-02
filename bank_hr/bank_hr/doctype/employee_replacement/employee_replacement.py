# Copyright (c) 2025, mina and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EmployeeReplacement(Document):
	def on_submit(self):
		employee_name = self.employee
		employee = frappe.get_doc("Employee",employee_name)
		employee.db_set("branch", self.to_branch, update_modified=False)
		#Branch
		report_to, default_shift = frappe.db.get_value('Branch', self.to_branch, ['custom_reports_to', 'custom_default_shift'])
		print("=========>",report_to)
		employee.db_set("reports_to", report_to, update_modified=False)
		employee.db_set("default_shift", default_shift, update_modified=False)
		############
		employee_name_second_branch = self.replace_with_employee
		employee2 = frappe.get_doc("Employee",employee_name_second_branch)
		employee2.db_set("branch", self.from_branch, update_modified=False)
		report_to2, default_shift2 = frappe.db.get_value('Branch', self.from_branch, ['custom_reports_to', 'custom_default_shift'])
    #Branch
		employee2.db_set("reports_to", report_to2, update_modified=False)
		employee2.db_set("default_shift", default_shift2, update_modified=False)
		frappe.msgprint(f"Employee {employee_name} Assigned to Branch {self.to_branch} , Employee {employee_name_second_branch} Assigned to Branch {self.from_branch}")
		# print("=========>",employee.as_dict())