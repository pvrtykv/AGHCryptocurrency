import {BlockHeader} from "./block-header";

export interface Block {
  timestamp: number,
  previous_block_hash: string,
  merkle_root: string
  difficulty: number,
  nonce: number,
  hash: string
}

