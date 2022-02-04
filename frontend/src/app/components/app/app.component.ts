import {Component, ViewChild} from '@angular/core';
import {BlockchainComponent} from "../blockchain/blockchain.component";
import {UnverifiedTransactionsComponent} from "../unverified-transactions/unverified-transactions.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  @ViewChild(BlockchainComponent) blockchain?: BlockchainComponent
  @ViewChild(UnverifiedTransactionsComponent) unverifiedTransactions?: UnverifiedTransactionsComponent

  refresh(): void {
    this.blockchain?.refresh()
    this.unverifiedTransactions?.refresh()
  }
}
