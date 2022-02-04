import {Component, EventEmitter, Output} from '@angular/core';
import {Transaction} from "../../model/transaction";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-add-transaction',
  templateUrl: './add-transaction.component.html',
  styleUrls: ['./add-transaction.component.css']
})
export class AddTransactionComponent {
  private httpClient: HttpClient
  form: FormGroup
  @Output()
  refresh: EventEmitter<any>

  constructor(formBuilder: FormBuilder, httpClient: HttpClient) {
    this.form = formBuilder.group({
      sender: ['', Validators.required],
      recipient: ['', Validators.required],
      amount: ['', Validators.required]
    })
    this.httpClient = httpClient
    this.refresh = new EventEmitter<any>()
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
        next: response => {
          this.refresh.emit(undefined)
          this.form.reset()
        },
        error: error => {}
      })
  }
}
