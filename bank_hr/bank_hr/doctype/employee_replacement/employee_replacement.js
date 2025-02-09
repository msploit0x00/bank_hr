// Copyright (c) 2025, mina and contributors
// For license information, please see license.txt

// Copyright (c) 2025, Mina and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Replacement", {
  to_branch: function(frm) {
      let branch = frm.doc.to_branch;

      frappe.db.get_list("Employee", { 
          filters: { "branch": branch }, 
          fields: ["name"]
      }).then(employees => {
          let employee_names = employees.map(emp => emp.name); // Extract names

          console.log("Employees:", employee_names);

          frm.set_query("replace_with_employee", function() {
              return {
                  filters: {
                      name: ["in", employee_names]
                  }
              };
          });
      });
  }
});

