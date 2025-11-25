from app.database import Database
import os

def test_database():
    print("Testing Database...")
    db = Database()
    
    # Test EcoPuntos
    print("\nTesting EcoPuntos...")
    initial_locations = len(db.get_saved_locations())
    db.add_saved_location("Test Point", "123 Test St", "recycling")
    new_locations = len(db.get_saved_locations())
    
    if new_locations == initial_locations + 1:
        print("✅ EcoPunto added successfully")
    else:
        print("❌ Failed to add EcoPunto")
        
    # Test Rewards
    print("\nTesting Rewards...")
    # Add tokens first
    db.add_eco_tokens(1000)
    initial_rewards = len(db.get_redeemed_rewards())
    success = db.redeem_reward("test_reward", "Test Reward", 100)
    
    if success:
        print("✅ Reward redeemed successfully")
        if len(db.get_redeemed_rewards()) == initial_rewards + 1:
             print("✅ Reward recorded in history")
        else:
             print("❌ Reward not recorded in history")
    else:
        print("❌ Failed to redeem reward")
        
    print("\nDatabase verification complete.")

if __name__ == "__main__":
    test_database()
