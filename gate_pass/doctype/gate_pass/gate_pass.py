# Copyright (c) 2023, Ashuar and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals

import json

import frappe
from frappe import _
from frappe.model.document import Document

class GatePass(Document):
	pass


@frappe.whitelist()
def create_gate_pass(po_name):
    # Fetch relevant information from the Purchase Order
    po = frappe.get_doc("Purchase Order", po_name)
    
    # Create a new Gate Pass document
    # existing_gate_pass = frappe.get_all("Gate Pass", filters = {"po_name", po_name}, limit =1 )

    # if existing_gate_pass:
    #     return{"error": "Gate Pass is already created"}
    gate_pass = frappe.new_doc("Gate Pass")
    gate_pass.po_name = po_name
    gate_pass.supplier = po.supplier_name
    gate_pass.purchase_order_date = po.transaction_date

    # Copy items from Purchase Order to Gate Pass
    for item in po.items:
        gate_pass.append("items", {
            "item_code": item.item_code,
            "qty": item.qty,
            "item_name": item.item_name,
            "schedule_date": item.schedule_date,
            "uom":item.uom,
            "description": item.description,
            "conversion_factor": item.conversion_factor,
            "rate": item.rate,
            "amount":item.amount,
            "base_rate": item.base_rate,
            "base_amount": item.base_amount
            # Add other relevant fields as needed
        })

    # Save the Gate Pass document
    
    gate_pass.insert()
    document_url = frappe.utils.get_url_to_form("Gate Pass", gate_pass.name)
    # Return the newly created Gate Pass document name
    return {"name": gate_pass.name, "url": document_url}
