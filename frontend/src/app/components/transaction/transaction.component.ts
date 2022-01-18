import { Component } from '@angular/core';
import {Transaction} from "../../model/transaction";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent {
  private httpClient: HttpClient
  form: FormGroup

  constructor(formBuilder: FormBuilder, httpClient: HttpClient) {
    this.form = formBuilder.group({
      sender: ['', Validators.required],
      recipient: ['', Validators.required],
      amount: ['', Validators.required]
    })
    this.httpClient = httpClient
  }

  makeTransaction() {
    if (this.form.invalid) {
      console.log("invalid form");
      return
    }
    const transaction = new Transaction(
      this.form.value.sender,
      this.form.value.recipient,
      this.form.value.amount
    )
    console.log(transaction)
    // POST
    this.httpClient.post("/api/blockchain/add_transaction", transaction)
      .subscribe({
        next: response => {alert("added transaction")},
        error: error => {}
      })
  }
}
