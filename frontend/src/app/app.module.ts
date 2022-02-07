import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app/app.component';
import { BlockchainComponent } from './components/blockchain/blockchain.component';
import {HttpClientModule} from "@angular/common/http";
import { BlockComponent } from './components/block/block.component';
import { AddTransactionComponent } from './components/add-transaction/add-transaction.component';
import {ReactiveFormsModule} from "@angular/forms";
import { UnverifiedTransactionsComponent } from './components/unverified-transactions/unverified-transactions.component';
import { TransactionComponent } from './components/transaction/transaction.component';
import { NavComponent } from './components/nav/nav.component';
import { MineBlockComponent } from './components/mine-block/mine-block.component';

@NgModule({
  declarations: [
    AppComponent,
    BlockchainComponent,
    BlockComponent,
    AddTransactionComponent,
    UnverifiedTransactionsComponent,
    TransactionComponent,
    NavComponent,
    MineBlockComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        ReactiveFormsModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
