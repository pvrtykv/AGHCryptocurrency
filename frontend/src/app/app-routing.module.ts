import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {BlockchainComponent} from "./components/blockchain/blockchain.component";
import {UnverifiedTransactionsComponent} from "./components/unverified-transactions/unverified-transactions.component";

const routes: Routes = [
  {path: 'blockchain', component: BlockchainComponent},
  {path: 'transactions', component: UnverifiedTransactionsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
