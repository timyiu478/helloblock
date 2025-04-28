async function main() {
   const HelloBlock = await ethers.getContractFactory("HelloBlock");

   // Start deployment, returning a promise that resolves to a contract object
   const hello_block = await HelloBlock.deploy();   
   console.log("Contract deployed to address:", hello_block.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });
