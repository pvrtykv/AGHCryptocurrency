import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Block} from "../../model/block";

@Component({
  selector: 'app-blockchain',
  templateUrl: './blockchain.component.html',
  styleUrls: ['./blockchain.component.css']
})
export class BlockchainComponent {
  blocks: Block[]

  constructor(private readonly httpClient: HttpClient) {
    this.blocks = []
  }

  ngOnInit(): void {
    this.refresh()
  }

  refresh(): void {
    this.httpClient.get("/api/blockchain/show_chain")
      .subscribe({next: (value: any) => { this.blocks = value as Block[]},
        error: (error: any) => {}
      })
  }

}
