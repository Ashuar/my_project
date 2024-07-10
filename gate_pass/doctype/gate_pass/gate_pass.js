// Copyright (c) 2024, Ashuar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gate Pass', {
	refresh: function(frm) {
      frm.add_custom_button(__('New Button'), function(){
        alert('button is clicked')
      })
	}
});

frappe.ui.form.on('Purchase Order', {
    refresh: function(frm) {
      if (frm.doc.docstatus === 1) {
        frm.add_custom_button(__('Create Gate Pass'), function() {


          frappe.call({
            method: 'my_project.gate_pass.doctype.gate_pass.gate_pass.create_gate_pass',
            args: {
                po_name: frm.doc.name
            },
            callback: function (r) {
                if (r.message) {
                    frappe.msgprint(__('Gate Pass created: {0}', [r.message]));
                } else {
                    frappe.msgprint(__('Failed to create Gate Pass.'));
                }
            }
        });
          // createGatePass(frm);
        }, __('Create'));
      }
    }
  });
// 
// function createGatePass(frm) {
    // frappe.call({
        // method: 'my_project.gate_pass.doctype.gate_pass.create_gate_pass',
        // args: {
            // po_name: frm.doc.name
        // },
        // callback: function (r) {
            // if (r.message) {
                // frappe.msgprint(__('Gate Pass created: {0}', [r.message]));
            // } else {
                // frappe.msgprint(__('Failed to create Gate Pass.'));
            // }
        // }
    // });
// }

