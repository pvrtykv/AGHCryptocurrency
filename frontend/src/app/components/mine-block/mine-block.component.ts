import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-mine-block',
  templateUrl: './mine-block.component.html',
  styleUrls: ['./mine-block.component.css']
})
export class MineBlockComponent {
  private httpClient: HttpClient
  @Output()
  refresh: EventEmitter<any>

  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient
    this.refresh = new EventEmitter<any>()
  }
  mineBlock(){
    this.httpClient.get("api/blockchain/mine_block")
      .subscribe({
        next: (response: any) => {
          this.refresh.emit(undefined)
        },
        error: message => {}
      })
  }
}
