import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app/app.component';
import { BlockchainComponent } from './components/blockchain/blockchain.component';
import {HttpClientModule} from "@angular/common/http";
import { BlockComponent } from './components/block/block.component';
import { TransactionComponent } from './components/transaction/transaction.component';
import {ReactiveFormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    BlockchainComponent,
    BlockComponent,
    TransactionComponent
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
