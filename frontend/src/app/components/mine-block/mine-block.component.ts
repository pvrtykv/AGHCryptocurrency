import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-mine-block',
  templateUrl: './mine-block.component.html',
  styleUrls: ['./mine-block.component.css']
})
export class MineBlockComponent {
  private httpClient: HttpClient
  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient
  }
  mineBlock(){
    this.httpClient.get("api/blockchain/mine_block")
  }
}
