import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Transaction} from "../../model/transaction";

@Component({
  selector: 'app-unverified-transactions',
  templateUrl: './unverified-transactions.component.html',
  styleUrls: ['./unverified-transactions.component.css']
})

export class UnverifiedTransactionsComponent implements OnInit {
  transactions: Transaction[]

  constructor(private readonly httpClient: HttpClient) {
    this.transactions = []
  }

  ngOnInit(): void {
    this.refresh()
  }

  refresh(): void {
    this.httpClient.get("api/blockchain/show_unverified_transactions")
      .subscribe({
        next: (value: any) => {this.transactions = value as Transaction[]
          console.log(value)},
        error: (error: any) => {}
      })
  }

}
